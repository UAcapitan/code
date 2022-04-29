<?php

namespace App\Entity;

use App\Repository\ImageRepository;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=ImageRepository::class)
 */
class Image
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=500)
     */
    private $link;

    /**
     * @ORM\ManyToOne(targetEntity=Campaigns::class, inversedBy="images")
     * @ORM\JoinColumn(nullable=false)
     */
    private $campaigns;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getLink(): ?string
    {
        return $this->link;
    }

    public function setLink(string $link): self
    {
        $this->link = $link;

        return $this;
    }

    public function getCampaigns(): ?Campaigns
    {
        return $this->campaigns;
    }

    public function setCampaigns(?Campaigns $campaigns): self
    {
        $this->campaigns = $campaigns;

        return $this;
    }
}
