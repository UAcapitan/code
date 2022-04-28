<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\User;
use App\Entity\Campaigns;
use App\Entity\BonusesUser;

class UserPageController extends AbstractController
{
    /**
     * @Route("/user/{id}", name="user_info")
     */
    public function index(int $id): Response
    {
        $user = $this->getDoctrine()->getRepository(User::class)->find($id);
        $campaigns = $this->getDoctrine()->getRepository(Campaigns::class)->findBy(['user' => $id], ['id' => 'DESC']);
        $bonuses = $this->getDoctrine()->getRepository(BonusesUser::class)->findBy(['user' => $id]);

        if ($user == $this->getUser()) {
            $check_user = true;
        } else {
            $check_user = false;
        }

        return $this->render('user_page/index.html.twig', [
            'user' => $user,
            'campaigns' => $campaigns,
            'bonuses' => $bonuses,
            'check_user' => $check_user,
        ]);
    }
}
